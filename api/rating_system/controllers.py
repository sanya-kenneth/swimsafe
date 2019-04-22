from api.database.db import db
from api.rating_system.models import RateTrainer
from api.auth.utilities import validateUser
from api.trainers.models import Trainer
from flask import jsonify, request


validate_user = validateUser()


def rate_trainer(current_user, trainer_id):
    data = request.get_json()
    user_rating = data.get('user_rating')
    validate_user.check_user_is_loggedin(current_user)
    if current_user.account_type == "admin":
        return jsonify({'message': 'You are not allowed to perform this action',
                        'status': 403})
    try:
        int(user_rating)
    except:
        return jsonify({'message': 'user rating must be a valid number',
                        'status': 400})
    rating_allowed = [1, 2, 3, 4, 5]
    if user_rating not in rating_allowed:
        return jsonify({'message': 'Invalid rating. Only numbers 1-5 are allowed',
                        'status': 400})
    # Get the trainer the user intends to rate
    retrieve_trainer = Trainer.query.filter_by(trainer_id=trainer_id).first()
    if not retrieve_trainer:
        return jsonify({'message': 'Trainer was not found', 'status': 404})
    # check if user already rated this trainer
    retrieve_rating = RateTrainer.query.all()
    for rating in retrieve_rating:
        print(type(trainer_id))
        if int(rating.user_id) == int(current_user.user_id) and rating.trainer_id == int(trainer_id):
            rating_id = rating.rate_id
            print(rating_id)
            # get the user rating
            new_rating = RateTrainer.query.filter_by(rate_id=rating_id).first()
            setattr(new_rating, 'trainer_rating', user_rating)
            db.session.commit()
            return jsonify({'message': 'We have updated your rating to this Trainer',
                            'status': 202})
    # Add new rating if the user has never rated the trainer
    make_rating = RateTrainer(trainer_rating=user_rating,
                              user_id=current_user.user_id, trainer_id=trainer_id)
    db.session.add(make_rating)
    db.session.commit()
    return jsonify({'message': 'We have recorded your rating to this Trainer',
                    'status': 201})


def retrieve_trainer_rating(current_user, trainer_id):
    validate_user.check_user_is_loggedin(current_user)
    # get all trainer ratings
    trainer_rate = RateTrainer.query.filter_by(trainer_id=trainer_id).all()
    if trainer_rate:
        # count the number of users who rated the trainer
        count_ratings = db.session.query(RateTrainer).filter_by(
            trainer_id=trainer_id).count()
        # List to hold trainer rating
        hold_rating = []
        # get trainer rating and add it to the list
        for rate in trainer_rate:
            hold_rating.append(rate.trainer_rating)
        # calculate the total of the trainer_rating
        total_of_trainer_rating = sum(hold_rating)
        # calculate the average rating for the trainer
        final_rating = total_of_trainer_rating/count_ratings
        return jsonify({'trainer_rating': final_rating, 'status': 200})

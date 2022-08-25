from src import db
from src.database import models
# from sqlalchemy import and_

# films = db.session.query(models.Film).all()
# print(films)
# print('-' * 80)
# films_order_rat = db.session.query(models.Film).order_by(models.Film.rating).all()
# print(films_order_rat)
# print('-' * 80)
# films_order_rat_desc = db.session.query(models.Film).order_by(models.Film.rating.desc()).all()
# print(films_order_rat_desc)
# print('-' * 80)
# harry_pot_and_ch_s = db.session.query(models.Film).filter(
#     models.Film.title == 'Harry Potter and Chamber of Secrets'
# ).first()
# print(harry_pot_and_ch_s)
# print('-' * 80)
# harry_pot_and_priz_az = db.session.query(models.Film).filter_by(
#     title='Harry Potter and the Prizoner of Azkaban'
# ).first()
# print(harry_pot_and_priz_az)
# print('-' * 80)
# and_statement_harry_p = db.session.query(models.Film).filter(
#     models.Film.title != 'Harry Potter and Chamber of Secrets',
#     models.Film.rating >= 7.5
# ).all()
# print(and_statement_harry_p)
# print('-'*80)
# and_statement_harry_p_v2 = db.session.query(models.Film).filter(
#     models.Film.title != 'Herry Potter and Chamber of Secrets'
# ).filter(models.Film.rating >= 7.5).all()
# print(and_statement_harry_p_v2)
# print('-' * 80)
# and_statement_harry_p_v3 = db.session.query(models.Film).filter(
#     and_(
#         models.Film.title != 'Harry Potter and Chamber of Secrets',
#         models.Film.rating >= 7.5
#     )
# ).all()
# print(and_statement_harry_p_v3)
# print('-' * 80)
# deathly_hallows = db.session.query(models.Film).filter(
#     models.Film.title.like('%Deathly Hallows%')
# ).all()
# print(deathly_hallows)
# print('-'*80)
# deathly_hallows_register_not_sens = db.session.query(models.Film).filter(
#     models.Film.title.ilike('%deathly HALLOWS%')
# ).all()
# print(deathly_hallows_register_not_sens)
# print('-'*80)
# harry_pot_sorted_by_length = db.session.query(models.Film).filter(
#     models.Film.length.in_([146, 161])
# ).all()
# print(harry_pot_sorted_by_length)
harry_pot_sorted_by_length = db.session.query(models.Film).filter(
    ~models.Film.length.in_([146, 161])
).all()
print(harry_pot_sorted_by_length)
print('-'*80)
harry_pot_sorted_by_length_lim = db.session.query(models.Film).filter(
    ~models.Film.length.in_([146, 161])
).all()[:2]
print(harry_pot_sorted_by_length_lim)
print('-'*80)
films_with_actors = db.session.query(models.Film).join(models.Film.actors).all()
print(films_with_actors)

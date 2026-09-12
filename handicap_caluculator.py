from database import insert_round, insert_range_session, get_club_average, get_all_rounds

def calculate_handicap_index(course_rating, slope_rating, total_score):
    rounds = get_all_rounds()

    if len(rounds) < 8:
        return None

    score_differential = (113/slope_rating) * (total_score - course_rating)

    
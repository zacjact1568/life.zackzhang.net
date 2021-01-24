from utils.time import current_year


def base(request):
    return {'copyright_to_year': current_year()}

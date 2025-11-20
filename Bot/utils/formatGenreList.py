def formatGenreList(genres):
    return ''.join([f'{i}: {genre[1]}\n' for i, genre in enumerate(genres)])
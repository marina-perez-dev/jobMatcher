from utils.rome_utils import load_rome_local, filter_metiers

def search_rome(keyword):
    metiers = load_rome_local()
    return filter_metiers(keyword, metiers)

def paginate_results(results, page, page_size=10):
    start = page * page_size
    end = start + page_size
    return results[start:end], start, end, len(results)

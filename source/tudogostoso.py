import requests



def get_recipe_tudogostoso(id):
    url = 'https://api.tudogostoso.com.br/api/v3/recipes/{}'.format(id)
    headers = {
        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 7.1.2; G011A Build/N2G48H)',
        'Authorization': 'Token token=4ecfd71f20ddf4011acd349edandroid',
        'Cookie': '_tdg_sesssion=63a36bd3521b82463d8e0c247f94fc85'
    }
    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        if res.status_code == 200:
            return res.json()
        elif res.status_code == 302:
            return 302
        else:
            print('status code != 200 && != 302 ... {}'.format(res.status_code))
    except Exception as err:
        print('exp get recipe tudogostoso ... {}'.format(err))
    return False
import requests

petition_time_out = 15 * 60


def send_petition(url, method="GET", params=None, data={}, json_data={}, headers={}, timeout=petition_time_out):
    response = None
    petition_url = url
    try:
        response = requests.request(method, petition_url, params=params, data=data,
                                    json=json_data, headers=headers, timeout=timeout)
        return response
    except (TypeError, ValueError) as e:
        if response:
            return response
        else:
            return False
    except Exception as e:
        return False

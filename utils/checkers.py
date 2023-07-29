def validate_request(func):
    def wrapper(*args, **kwargs):
        status = kwargs.get("exp_status") or "success"
        method = kwargs.get("data").get("method", None)
        _id = kwargs.get("data").get("id", None)
        request = func(*args, **kwargs)
        assert request.get("id") == _id, "Id в запросе и ответе не совпадают"
        assert request.get("method") == method, "Method в запросе и ответе не совпадают"
        if method != "select":
            assert (
                request.get("status") == status
            ), f"Фактический статус: \"{request.get('status')}\" не соответствует ожидаемому {status}"
        return request

    return wrapper

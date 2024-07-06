class TestAuthData:
    lg = "murfl@te.com"
    ps = '234634'
    fn = "Burfl"
    token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY2NzdlN2IwOWVkMjgwMDAxYjQ0ODQzYyIsImlhdCI6MTcxOTEzNDEyOCwiZXhwIjoxNzE5MTM1MzI4fQ.qtM72wEm4zgHDhtqoHXbuM4a0rFgEOELo4QRz0pYVdI'

    dat = {
        "email": "pulyad@tu.com",
        "password": "2834634",
        "name": "Yohanf"
    }

    dat1 = {
        "email": "",
        "password": "2834634",
        "name": "Yohanf"
    }

    dat2 = {
        "email": "pulyad@tu.com",
        "password": "",
        "name": "Yohanf"
    }

    dat3 = {
        "email": "pulyad@tu.com",
        "password": "2834634",
        "name": ""
    }

    dat4 = {
        "email": "",
        "password": "2834634"
    }

    dat5 = {
        "email": "pulyad@tu.com",
        "password": ""
    }

    dat6 = {
        "email": "pulyad@tu.com",
        "password": "2834634"
    }

    order = {
        "ingredients": ["61c0c5a71d1f82001bdaaa70", "61c0c5a71d1f82001bdaaa74"]
    }

    order1 = {
        "ingredients": []
    }

    order2 = {
        "ingredients": ["gjhfdjdhfhfh"]
    }

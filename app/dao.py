def load_categories():
    return [{
        'id': 1,
        'name': 'Mobile'
    },{
        'id': 2,
        'name': 'Tablet'
    }]
def load_products(kw=None):
    products = [{
        'id': 1,
        'name': 'iPhone 16',
        'price': 20000000,
        'image': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fvtv.vn%2Fcong-nghe%2Fiphone-16-se-co-chip-a18-va-a18-pro-20231024143238614.htm&psig=AOvVaw20OkVQQbyrz0bn3RJc6_6T&ust=1698304563725000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCNjP99fTkIIDFQAAAAAdAAAAABAD'
    }, {
        'id': 2,
        'name': 'Galaxy s22 ultra ',
        'price': 99999999,
        'image': 'https://cdn.tgdd.vn/Products/Images/42/251192/iphone-14-pro-max-vang-thumb-600x600.jpg'
    }]
    if kw:
        products = [p for p in products if p['name'].find(kw) >= 0]

    return products
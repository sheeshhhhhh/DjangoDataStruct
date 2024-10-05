from django.shortcuts import render

# Create your views here.

def portfolio_views(request):
    staticPhoto = [
        {'name': 'Java',         'link': 'photo/icon8-java.svg',          'urlTo': 'https://www.java.com/en/'},
        {'name': 'NestJS',       'link': 'photo/icon8-nestjs.svg',        'urlTo': 'https://nestjs.com/'},
        {'name': 'CSS',          'link': 'photo/icons8-css.svg',          'urlTo': 'https://developer.mozilla.org/en-US/docs/Web/CSS'},
        {'name': 'HTML',         'link': 'photo/icons8-html.svg',         'urlTo': 'https://developer.mozilla.org/en-US/docs/Web/HTML'},
        {'name': 'JavaScript',   'link': 'photo/icons8-javascript.svg',   'urlTo': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript'},
        {'name': 'TypeScript',   'link': 'photo/icons8-typescript.svg',   'urlTo': 'https://www.typescriptlang.org/'},
        {'name': 'Node.js',      'link': 'photo/icons8-node-js.svg',      'urlTo': 'https://nodejs.org/'},
        {'name': 'PostgreSQL',   'link': 'photo/icons8-postgresql.svg',   'urlTo': 'https://www.postgresql.org/'},
        {'name': 'Mongo DB',     'link': 'photo/icons8-mongodb.svg',      'urlTo': 'https://www.mongodb.com/'},
        {'name': 'Prisma',       'link': 'photo/icons8-prisma.svg',       'urlTo': 'https://www.prisma.io/'},
        {'name': 'Tailwind CSS', 'link': 'photo/icons8-tailwind-css.svg', 'urlTo': 'https://tailwindcss.com/'}
    ]

    socials = [
        {'name': 'Instagram', 'link': 'photo/socials/icons8-instagram.svg', 'urlTo': 'URL_ADDRESS'},
        {'name': 'X',         'link': 'photo/socials/icons8-x-logo.svg',    'urlTo': 'URL_ADDRESS'},
        {'name': 'Facebook',  'link': 'photo/socials/icons8-facebook.svg',  'urlTo': 'URL_ADDRESS'},
        {'name': 'GitHub',    'link': 'photo/socials/icons8-github.svg',    'urlTo': 'URL_ADDRESS'},
    ]

    return render(request, 'portfolio.html', {
        "technologies": staticPhoto,
        "socials": socials
    })
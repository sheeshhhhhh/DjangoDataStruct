from django.shortcuts import render

# Create your views here.

def portfolio_views(request):
    staticPhoto = [
        {'name': 'Java',         'link': 'photo/icon8-java.svg',          'urlTo': 'https://www.java.com/en/'},
        {'name': 'NestJS',       'link': 'photo/icon8-nestjs.svg',        'urlTo': 'https://nestjs.com/'},
        {'name': 'CSS',          'link': 'photo/icons8-css.svg',          'urlTo': 'https://developer.mozilla.org/en-US/docs/Web/CSS'},
        {'name': 'HTML',         'link': 'photo/icons8-html.svg',         'urlTo': 'https://developer.mozilla.org/en-US/docs/Web/HTML'},
        {'name': 'React',        'link': 'photo/icons8-react.svg',        'urlTo': 'https://react.dev/'},
        {'name': 'JavaScript',   'link': 'photo/icons8-javascript.svg',   'urlTo': 'https://developer.mozilla.org/en-US/docs/Web/JavaScript'},
        {'name': 'TypeScript',   'link': 'photo/icons8-typescript.svg',   'urlTo': 'https://www.typescriptlang.org/'},
        {'name': 'Node.js',      'link': 'photo/icons8-node-js.svg',      'urlTo': 'https://nodejs.org/'},
        {'name': 'PostgreSQL',   'link': 'photo/icons8-postgresql.svg',   'urlTo': 'https://www.postgresql.org/'},
        {'name': 'Mongo DB',     'link': 'photo/icons8-mongodb.svg',      'urlTo': 'https://www.mongodb.com/'},
        {'name': 'Prisma',       'link': 'photo/icons8-prisma.svg',       'urlTo': 'https://www.prisma.io/'},
        {'name': 'Tailwind CSS', 'link': 'photo/icons8-tailwind-css.svg', 'urlTo': 'https://tailwindcss.com/'},
        {'name': 'git',          'link': 'photo/icons8-git.svg',          'urlTo': 'https://git-scm.com/'}
    ]

    socials = [
        {'name': 'Instagram', 'link': 'photo/socials/icons8-instagram.svg', 'urlTo': 'https://legitpinoy.com/wp-content/uploads/2024/06/FIJaybeeSucal-1.webp'},
        {'name': 'X',         'link': 'photo/socials/icons8-x-logo.svg',    'urlTo': 'https://x.com/Renn65759632'},
        {'name': 'Facebook',  'link': 'photo/socials/icons8-facebook.svg',  'urlTo': 'https://www.facebook.com/santos.renato44'},
        {'name': 'GitHub',    'link': 'photo/socials/icons8-github.svg',    'urlTo': 'https://github.com/sheeshhhhhh'},
        {'name': 'Dev.to',    'link': 'photo/socials/icons8-dev-dot-to.svg', 'urlTo': 'https://dev.to/renn'}
    ]

    return render(request, 'portfolio.html', {
        "technologies": staticPhoto,
        "socials": socials
    })
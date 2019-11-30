# BlogApp - <Powered by Django> 


# Main Freatures!

  - Create or update your blog posts. Comment the posts and join the thread mechanism 
  - User authenticated web application that handles both authentication and authorization. 
  - The authentication system in Django aims to be very generic and doesn’t provide some features commonly found in web authentication systems. Solutions for some of these common problems have been implemented in third-party packages:

    -Password strength checking
    -Throttling of login attempts
    -Authentication against third-parties (OAuth, for example)
    -Object-level permissions

### Installation
Requires django-version<=1.9.13 and python2=2.7.9 or above.

```sh
$ pip install pip
$ pip install Django==1.9.13
```

#### third party apps Installation
| Apps | Links |
| ------| -----|
|Pagedown| <https://github.com/timmyomahony/django-pagedown> |
| Crispy-forms | <https://django-crispy-forms.readthedocs.io/en/latest/install.html> |
| Markdown-deux | <https://github.com/trentm/django-markdown-deux> |
| Pillow | <https://pillow.readthedocs.io/en/stable/installation.html> |
| Markdown2| <https://github.com/trentm/python-markdown2>(Depreciated)|


Clone the repository, 
```
$ git clone https://github.com/deepanshurana/BlogApp.git
```
##### Using Django....

```
$ cd BlogApp/blog
$ python manage.py makemigrations 
$ python manage.py migrate 
# python manage.py runserver 
```

### Todos

 - Add more functionalites, Profile editing is under process.
 - Adding more JavaScript code.

License
----
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)








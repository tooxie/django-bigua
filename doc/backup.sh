WORKING_DIRECTORY=`pwd`
cd ..
mv local_settings.py local_settings.p_y
tar cf doc/django-bigua.tar settings.py
find . -name '*.py' -exec tar rf ./doc/django-bigua.tar '{}' \;
find . -name '*.js' -exec tar rf ./doc/django-bigua.tar '{}' \;
find . -name '*.html' -exec tar rf ./doc/django-bigua.tar '{}' \;
find . -name '*.jpg' -exec tar rf ./doc/django-bigua.tar '{}' \;
find . -name '*.png' -exec tar rf ./doc/django-bigua.tar '{}' \;
find . -name '*.gif' -exec tar rf ./doc/django-bigua.tar '{}' \;
find . -name '*.css' -exec tar rf ./doc/django-bigua.tar '{}' \;
mv local_settings.p_y local_settings.py
cd $WORKING_DIRECTORY

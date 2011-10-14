==============
django-favicon
==============

helper to get favicon of any url, using Google Favicon Service
 

general instalation
===================

* using **easy_install**
  
  easyinstall django-favicon

* using **pip** 
  
  pip install django-favicon

* direct from repository
  
  pip install -e git+git://github.com/rmaceissoft/django-favicon#egg=django-favicon


django implementation
=====================


Configuration
-------------


#. Add the 'djfavicon' to INSTALL_APPS

Basic usage
-----------

You can use at template through favicon filter. Example::
  
     {% load djfavicon_tags %}
    
     <img src="{{ url|favicon }}" />
     

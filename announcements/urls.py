from django.conf.urls import url

from announcements.views import detail, dismiss
from announcements.views import CreateAnnouncementView, UpdateAnnouncementView
from announcements.views import DeleteAnnouncementView, AnnouncementListView

app_name = "announcements"


urlpatterns = [  # "",
    url(r"^$", AnnouncementListView.as_view(), name="list"),
    url(r"^announcement/create/$", CreateAnnouncementView.as_view(), name="create"),
    url(r"^announcement/(?P<pk>\d+)/$", detail, name="detail"),
    url(r"^announcement/(?P<pk>\d+)/hide/$", dismiss, name="dismiss"),
    url(r"^announcement/(?P<pk>\d+)/update/$", UpdateAnnouncementView.as_view(), name="update"),
    url(r"^announcement/(?P<pk>\d+)/delete/$", DeleteAnnouncementView.as_view(), name="delete"),
]

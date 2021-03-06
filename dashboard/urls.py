from django.conf.urls import url
from .views import DashboardView, SpeakersView, SpeakerDetailView, \
    SpeakerCreateView, SpeakerUpdateView, SpeakerDeleteView, LecturesView, \
    LectureCreateView, LectureDetailView, LectureUpdateView, LectureDeleteView, \
    CompanyView, CompanyCreateView, CompanyDetailView, CompanyUpdateView, \
    CompanyDeleteView, PlacesView, PlaceCreateView, \
    PlaceUpdateView, PlaceDeleteView, PartnerStatusesView, \
    PartnerStatusCreateView, PartnerStatusUpdateView, \
    PartnerStatusDeleteView, NewsesView, NewsCreateView, NewsDetailView, \
    NewsUpdateView, NewsDeleteView, PicturesView, PictureCreateView, \
    PictureDeleteView, DashboardLoginView, DashboardLogoutView, \
    PhotoDeleteView, PhotoCreateView, PhotoView

urlpatterns = [
    url(r'^$', DashboardView.as_view(), name='dashboard'),
    url(r'^login/$', DashboardLoginView.as_view(), name='login'),
    url(r'^logout/$', DashboardLogoutView.as_view(), name='logout'),
    url(r'^speakers/$', SpeakersView.as_view(), name='speaker_list'),
    url(r'^speakers/(?P<pk>\d+)$', SpeakerDetailView.as_view(), name='speaker_detail'),
    url(r'^speakers/create$', SpeakerCreateView.as_view(), name='speaker_create'),
    url(r'^speakers/(?P<pk>\d+)/edit$', SpeakerUpdateView.as_view(), name='speaker_edit'),
    url(r'^speakers/(?P<pk>\d+)/delete$', SpeakerDeleteView.as_view(), name='speaker_delete'),
    url(r'^lectures/$', LecturesView.as_view(), name='lecture_list'),
    url(r'^lectures/create$', LectureCreateView.as_view(), name='lecture_create'),
    url(r'^lectures/(?P<pk>\d+)$', LectureDetailView.as_view(), name='lecture_detail'),
    url(r'^lectures/(?P<pk>\d+)/edit$', LectureUpdateView.as_view(), name='lecture_edit'),
    url(r'^lectures/(?P<pk>\d+)/delete$', LectureDeleteView.as_view(), name='lecture_delete'),
    url(r'^companies/$', CompanyView.as_view(), name='company_list'),
    url(r'^companies/create$', CompanyCreateView.as_view(), name='company_create'),
    url(r'^companies/(?P<pk>\d+)$', CompanyDetailView.as_view(), name='company_detail'),
    url(r'^companies/(?P<pk>\d+)/edit$', CompanyUpdateView.as_view(), name='company_edit'),
    url(r'^companies/(?P<pk>\d+)/delete$', CompanyDeleteView.as_view(), name='company_delete'),
    url(r'^places$', PlacesView.as_view(), name='place_list'),
    url(r'^places/create$', PlaceCreateView.as_view(), name='place_create'),
    url(r'^places/(?P<pk>\d+)/edit$', PlaceUpdateView.as_view(), name='place_edit'),
    url(r'^places/(?P<pk>\d+)/delete$', PlaceDeleteView.as_view(), name='place_delete'),
    url(r'^partner_statuses$', PartnerStatusesView.as_view(), name='partner_status_list'),
    url(r'^partner_statuses/create$', PartnerStatusCreateView.as_view(), name='partner_status_create'),
    url(r'^partner_statuses/(?P<pk>\d+)/edit$', PartnerStatusUpdateView.as_view(), name='partner_status_edit'),
    url(r'^partner_statuses/(?P<pk>\d+)/delete$', PartnerStatusDeleteView.as_view(), name='partner_status_delete'),
    url(r'^news$', NewsesView.as_view(), name='news_list'),
    url(r'^news/create$', NewsCreateView.as_view(), name='news_create'),
    url(r'^news/(?P<pk>\d+)$', NewsDetailView.as_view(), name='news_detail'),
    url(r'^news/(?P<pk>\d+)/edit$', NewsUpdateView.as_view(), name='news_edit'),
    url(r'^news/(?P<pk>\d+)/delete$', NewsDeleteView.as_view(), name='news_delete'),
    url(r'^pictures$', PicturesView.as_view(), name='picture_list'),
    url(r'^pictures/upload', PictureCreateView.as_view(), name='picture_create'),
    url(r'^pictures/(?P<pk>\d+)/delete$', PictureDeleteView.as_view(), name='picture_delete'),
    url(r'^gallery$', PhotoView.as_view(), name='gallery_list'),
    url(r'^gallery/upload', PhotoCreateView.as_view(),
        name='gallery_create'),
    url(r'^gallery/(?P<pk>\d+)/delete$', PhotoDeleteView.as_view(),
        name='gallery_delete'),
]

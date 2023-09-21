from django.shortcuts import render
import folium
from account.models import UIPrefs
from . models import Mission

def index(request):
    try:
        preferred = UIPrefs.objects.all()[0]
    except Exception as e:
        preferred = {
            'latitude': '25.036289',
            'longitude': '-77.481326',
            'church_name': 'invalid',
            'church_address': 'invalid',
            'church_phone': 'invalid'
        }
        print(e)
    
    missions = Mission.objects.all()
    ourmap = folium.Map(location=[preferred.latitude, preferred.longitude], zoom_start=9)

    #Add home church location
    homeCoords = (preferred.latitude, preferred.longitude)
    hometooltip = "This is home"
    homeicon = folium.Icon(color='green', icon='fa-bars', prefix='fa')
    homeframe = folium.IFrame('Home: ' + preferred.church_name +
                              ' <a href=https://www.bible.com/>Bible.com</a> <br />' +
                              preferred.church_address + '<br />' +
                              preferred.church_phone)
    homepopup = folium.Popup(homeframe, min_width=300, max_width=300)
    folium.Marker(homeCoords,
                  tooltip=hometooltip,
                  icon=homeicon,
                  popup=homepopup).add_to(ourmap)

    if len(missions) > 0:
        for mission in missions:
            coordinates = (mission.latitude, mission.longitude)
            tooltip = "Hover message"
            icon = folium.Icon(color='lightgray', icon='fa-bars', prefix='fa')
            iframe = folium.IFrame('Mission name: ' + str(mission.location) + ' <a href=https://www.bible.com/>Bible.com</a>')
            popup = folium.Popup(iframe, min_width=300, max_width=300)

            folium.Marker(coordinates,
                        tooltip=tooltip,
                        icon=icon,
                        popup=popup).add_to(ourmap)

    context = {'map': ourmap._repr_html_()}
    if request.path == '/fullscreenmap/':
        #Fullscreen does not inherit from the base, otherwise it is the same
        return render(request, 'missionmap/fullscreen.html', context)

    return render(request, 'missionmap/index.html', context)

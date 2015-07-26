from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from actors.models import SubZone, Category, Amendity
from django.http import HttpResponse, HttpResponseNotFound
import json

class GetSubzoneScore(View):
    '''
    AJAX call to generate keys
    '''

    def get(self, request):
        scores = []
        data = request.GET
        subzone_name = str(data.get('subzone', None))
        try:
            subzone = SubZone.objects.get(name=subzone_name)
        except SubZone.DoesNotExist:
            print("SubZone does not exist")
            return HttpResponseNotFound(content=dict(error_code=404, error_msg="Deployment does not exist"));

        try:
            subzone_overall_score = subzone.overall_score
            categories = Category.objects.filter(subzone=subzone)

        except (ValueError, TypeError) as e:
            return HttpResponseNotFound(content=dict(error_code=402, error_msg="Subzone is invalid"));

        scores = {}
        response_data = {}

        scores['overall'] = subzone_overall_score
        for category in categories:
            scores[category.get_category_type_display()] = category.score

        response_data = {'name': subzone_name,
                        'scores': scores
                }

        return HttpResponse(json.dumps(response_data), content_type="application/json")



class MapView(TemplateView):

    template_name = 'pages/map.html'

    def get_town_info(self):
        towns = [] 
        current_town_name = ''
        subzone_name = ''
        subzone_info = []

        subzones = SubZone.objects.all().order_by('town_name', 'name')

        print(subzones)

        for subzone in subzones:
            if not current_town_name:
                print("start town:%s" % (subzone.get_town_name_display()))
                current_town_name = subzone.get_town_name_display()
                subzone_info.append({'name': subzone.name})
            elif current_town_name != subzone.get_town_name_display():
                print("old town %s new town: %s subzone %s" % (current_town_name, subzone.get_town_name_display(), subzone_info))
                towns.append({'name': current_town_name, 'subzones': subzone_info})
                current_town_name = subzone.get_town_name_display()
                subzone_info = []
                subzone_info.append({'name': subzone.name})
            else:
                print("adding into same town")
                subzone_info.append({'name': subzone.name})

        towns.append({'name': current_town_name, 'subzones': subzone_info})

        return {
                'towns': towns
        }

    def get_context_data(self, **kwargs):
        ctx = super(MapView, self).get_context_data(**kwargs)

        towns = self.get_town_info()
        print(towns)
        ctx.update(towns)
        return ctx

    def dispatch(self, *args, **kwargs):
        return super(MapView, self).dispatch(*args, **kwargs)
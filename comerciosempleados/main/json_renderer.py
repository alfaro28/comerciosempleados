from rest_framework import renderers


class JSONRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if data is None:
            response_data = {
                'rc': 0,
                'msg': 'Ok'
            }
        elif 'rc' in data:
            response_data = data
        else:
            response_data = {
                'rc': 0,
                'msg': 'Ok',
                'data': data,
            }

        response = super(JSONRenderer, self).render(response_data, accepted_media_type, renderer_context)

        return response

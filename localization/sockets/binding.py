from channels import binding
from ..models import CarStatus
from ..api.serializers import CarStatusModelSerializer


class CarStatusBinding(binding.WebsocketBinding):

    model = CarStatus
    stream = "status"
    fields = [
        'car_lat',
        'car_lon',
        'car_speed',
        'car_fuel',
        'car_temp',
        'car_status',
        'car_number',
        'car_driver_id']

    @classmethod
    def group_names(cls, instance):
        return ["status-updates"]

    def has_permission(self, user, action, pk):
        return True
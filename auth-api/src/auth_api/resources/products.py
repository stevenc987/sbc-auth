# Copyright © 2019 Province of British Columbia
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""API endpoints for managing a Product resource."""

import json

from flask_restplus import Namespace, Resource, cors

from auth_api import status as http_status
from auth_api.exceptions import BusinessException
from auth_api.services import Product as ProductService
from auth_api.tracer import Tracer
from auth_api.utils.util import cors_preflight


API = Namespace('products', description='Endpoints for products management')
TRACER = Tracer.get_instance()


@cors_preflight('GET,OPTIONS')
@API.route('', methods=['GET', 'OPTIONS'])
class Products(Resource):
    """Resource for managing products."""

    @staticmethod
    @TRACER.trace()
    @cors.crossdomain(origin='*')
    def get():
        """Get a list of all products."""
        try:
            response, status = json.dumps(ProductService.get_products()), http_status.HTTP_200_OK
        except BusinessException as exception:
            response, status = {'code': exception.code, 'message': exception.message}, exception.status_code
        return response, status

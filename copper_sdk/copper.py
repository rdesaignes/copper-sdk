from copper_sdk.notes import Notes
import requests, json
from .users import Users
from .leads import Leads
from .activities import Activities
from .companies import Companies
from .people import People
from .opportunities import Opportunities
from .customer_sources import CustomerSources
from .loss_reasons import LossReasons
from .custom_field_definitions import CustomFieldDefinitions
from .tasks import Tasks
from retry import retry
RETRY_COUNT = 5  # retry 5 times
RETRY_INTERVAL = 5 # retry with this interval seconds
RETRY_STATUS_CODE = [502,504]

class Copper():
    # Constructor - authentication details
    def __init__(self, token, email, base_url = None, debug = False, session = None):
        self.token = token
        self.email = email
        if base_url is None:
            self.base_url = "https://api.copper.com/developer_api/v1"
        else:
            self.base_url = base_url
        self.debug = debug

        # init request
        if not session:
            session = requests.Session()

        self.session = session
        self.session.headers = {}
        self.session.headers['X-PW-AccessToken'] = self.token
        self.session.headers['X-PW-Application'] = 'developer_api'
        self.session.headers['X-PW-UserEmail'] = self.email
        self.session.headers['Content-Type'] = 'application/json'
        self.retry_count = 0

    def get(self, endpoint):
        return self.api_call('get', endpoint)

    def post(self, endpoint, opts):
        return self.api_call('post', endpoint, opts)

    def put(self, endpoint, opts):
        return self.api_call('put', endpoint, opts)

    def delete(self, endpoint):
        return self.api_call('delete', endpoint)

    @retry(Exception, tries =RETRY_COUNT, delay=RETRY_INTERVAL)
    def get_response(self, method, endpoint, optsJson):
        """
            This function returns the api response
        """
        self.retry_count +=1
        print("Trying===> ",self.retry_count, " of " ,RETRY_COUNT)
        print("===base url", self.base_url)
        response = getattr(self.session, method)(self.base_url + endpoint, data=optsJson)
        print("=======Response code===>", response.status_code)
        if response.status_code in RETRY_STATUS_CODE and RETRY_COUNT != self.retry_count:
            raise Exception("Error at copper api call" + endpoint)
        return response

    def api_call(self, method, endpoint, opts = None):
        optsJson = None
        if opts:
            optsJson = json.dumps(opts)
            if self.debug:
              print(optsJson)

        # dynamically call method to handle status change
        self.retry_count = 0
        response = self.get_response(method, endpoint, optsJson)

        if self.debug:
          print(response.text)

        return json.loads(response.text)

    def users(self):
        return Users(self)

    def leads(self):
        return Leads(self)

    def activities(self):
        return Activities(self)

    def opportunities(self):
        return Opportunities(self)

    def people(self):
        return People(self)

    def companies(self):
        return Companies(self)

    def customersources(self):
        return CustomerSources(self)

    def lossreasons(self):
        return LossReasons(self)

    def customfielddefinitions(self):
        return CustomFieldDefinitions(self)

    def tasks(self):
        return Tasks(self)

    def notes(self):
        return Notes(self)
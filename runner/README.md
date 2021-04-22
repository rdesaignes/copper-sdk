# CopperSDK Runner

CopperSDK runner to test helper functions.

Install requirements using

`pip install -r requirements.txt`

It is required to provide an .env file at this path with following content:

```
TOKEN=[Your CopperCRM token]
EMAIL=[Your CopperCRM email]
TASK_ID=[A Task Id to perform examples]
LEAD_ID=[A Lead Id to perform examples]
OPPORTUNITY_ID=[An Opportunity Id to perform examples]
```

When executing examples, there could be a wait of 7 secs per examples, to let
CopperCRM reflect the changes.

# Available examples

## Notes

* Lead.
* Opportunity.
* Task.

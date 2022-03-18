## Common errors in Vlocity and Salesforce

1. This page has an error. You might just need to refresh it. [this.childInput.checkValidity is not a function] Failing descriptor: {markup://vlocity_cmt:omniscriptValidation}

Resolution: Remove the default code and update the js file with this - 

```js
import { LightningElement, api, wire, track } from "lwc";
import { OmniscriptBaseMixin } from "vlocity_cmt/omniscriptBaseMixin";

export default class <component_name> extends OmniscriptBaseMixin(LightningElement) {}
```

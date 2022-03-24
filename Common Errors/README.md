## Common errors in Vlocity and Salesforce

1. This page has an error. You might just need to refresh it. [this.childInput.checkValidity is not a function] Failing descriptor: {markup://vlocity_cmt:omniscriptValidation}

Resolution: Remove the default code and update the js file with this - 

```js
import { LightningElement, api, wire, track } from "lwc";
import { OmniscriptBaseMixin } from "vlocity_cmt/omniscriptBaseMixin";

export default class <component_name> extends OmniscriptBaseMixin(LightningElement) {}
```

2. This page has an error. You might just need to refresh it.
Attempting to reference cross-namespace module <component-name> in c-<component-name>
Failing descriptor: {c:tetsApp}

Follow the steps in this answer - https://ideas.salesforce.com/s/idea/a0B8W00000GdXQ3UAN/use-a-lightning-web-component-from-another-packagenamespace

Add <targets> in js-meta.xml and update Session Settings -> Use Lightning Web Security for Lightning web components.

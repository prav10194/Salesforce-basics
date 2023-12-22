## Common errors in Vlocity and Salesforce

1. This page has an error. You might just need to refresh it. [this.childInput.checkValidity is not a function] Failing descriptor: {markup://vlocity_cmt:omniscriptValidation}

Resolution: Remove the default code and update the js file with this - 

```js
import { LightningElement, api, wire, track } from "lwc";
import { OmniscriptBaseMixin } from "vlocity_cmt/omniscriptBaseMixin";

export default class <component_name> extends OmniscriptBaseMixin(LightningElement) {}
```

2. This page has an error. You might just need to refresh it.
Attempting to reference cross-namespace module component-name in c-component-name
Failing descriptor: {c:tetsApp}

Follow the steps in this answer - https://ideas.salesforce.com/s/idea/a0B8W00000GdXQ3UAN/use-a-lightning-web-component-from-another-packagenamespace

Add <targets> in js-meta.xml and update Session Settings -> Use Lightning Web Security for Lightning web components.

3. SFDX Commands not showing

In case sfdx commands are not showing in the command palette (Cmd + Shift + P), you need to check if you are in the correct folder. Make sure that the root directory you have open in VS Code contains an sfdx-project. json file.

![image](https://github.com/prav10194/Salesforce-basics/assets/8276139/15b97021-ec01-4539-ab42-8c5ca59b391f)


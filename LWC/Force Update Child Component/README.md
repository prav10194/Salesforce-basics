## Force re-render your child component if data is updated

#### This can be done by a work around of calling a method defined in child component from parent component 


Parent component 

```html
<template>
    <c-test-child-component childdata={parentdata}></c-test-child-component>
    <button onclick={updateChildComponent}>Update data</button>
</template>
```

```js
import { LightningElement, api, track } from "lwc";
import { OmniscriptBaseMixin } from "vlocity_cmt/omniscriptBaseMixin";

export default class Testlwc extends OmniscriptBaseMixin(LightningElement) {
    @track parentdata;

    connectedCallback(){
        this.parentdata = [1,2,3,4]
    }
    
    updateChildComponent = () => {
      this.template.querySelector('c-test-child-component').childfunction([4,3,2,1]);
    }
}
```

Child Component - testChildComponent

```html
<template>
    <div>{childdata}</div>
</template>
```

```js
import { LightningElement, api, track } from "lwc";
import { OmniscriptBaseMixin } from "vlocity_cmt/omniscriptBaseMixin";

export default class TestChildComponent extends OmniscriptBaseMixin(LightningElement) {
    
    @api childdata;
    @track childdata;

    @api 
    childfunction(parentdata){
        this.childdata = parentdata
    }
}
```

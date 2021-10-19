## Communication from Grand Child to Parent

We will create 3 components namely - parent, child and grand child. We will create an event in grand child and try to handle the event in parent component. 

#### Parent

HTML

```html
<template>
    <!-- <button>Get message from Grand child</button> -->
    <c-communication-child-l-w-c></c-communication-child-l-w-c>
    <p>{evtMessage}</p>
</template>
```

JS

```js
import { LightningElement, api, wire, track } from "lwc";
import { OmniscriptBaseMixin } from "vlocity_cmt/omniscriptBaseMixin";

export default class CommunicationParentLWC extends OmniscriptBaseMixin(LightningElement) {

    @track evtMessage;
    connectedCallback(){
        console.log("Parent component");
        this.template.addEventListener('btnclick', this.handleClick.bind(this));
    }

    handleClick(event){
        console.log("event.detail: ", JSON.stringify(event.detail));
        this.evtMessage = event.detail;
    }
}
```

#### Child

HTML

```html
<template>
    <c-communication-grand-child-l-w-c></c-communication-grand-child-l-w-c>
</template>
```

JS

```js
import { LightningElement, api, wire, track } from "lwc";
import { OmniscriptBaseMixin } from "vlocity_cmt/omniscriptBaseMixin";

export default class CommunicationChildLWC extends OmniscriptBaseMixin(LightningElement) {

    connectedCallback(){
        console.log("Child component");
    }
}
```


#### Grand Child

HTML

```html
<template>
    <button onclick={handleClick}>Get message from Grand child</button>
</template>
```

JS

```js
import { LightningElement, api, wire, track } from "lwc";
import { OmniscriptBaseMixin } from "vlocity_cmt/omniscriptBaseMixin";

export default class CommunicationGrandParentLWC extends OmniscriptBaseMixin(LightningElement) {

    @track evtMessage = 'Grand Child component event is triggered. ';

    connectedCallback(){
        console.log("Grand Child component");
    }

    handleClick(event){
        this.dispatchEvent(new CustomEvent('btnclick', { bubbles: true , composed : true, detail: this.evtMessage }));
    }
}
```

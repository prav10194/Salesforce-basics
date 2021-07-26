## From parent-to-child

Read more on this [here](https://developer.salesforce.com/docs/component-library/documentation/en/lwc/lwc.events_create_dispatch)
<br/>
Also refer to [this](https://medium.com/salesforce-champion/lwc-way-to-pass-the-data-between-component-parent-to-child-and-child-to-parent-component-6d8070ef4185)


#### Parent Component

The HTML looks like this

```html
<lightning-card  title="Parent Component">
        <c-child-component username="John Doe"></c-child-component>
</lightning-card>
```


#### Child Component

The HTML and JS looks like this

```html
<template>
    <lightning-card title="Child Component">
        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Welcome, {username}
    </lightning-card>
</template>
```

```js
import { LightningElement, track, api } from 'lwc';

export default class ChildComponent extends LightningElement {
    @api username;
}
```

## From child-to-parent

Child to parent communication involves using Events. Example is shown below - 

#### Parent Component

The HTML and JS looks like this

```html
<template>
    <lightning-card  title="Parent Component">
        <c-child-component username="John Doe" onchild={handleChild}></c-child-component>
        <p style="padding-left: 1rem;">Phone number: {childnumber}</p>
    </lightning-card>
</template>
```

```js
import { LightningElement, track } from 'lwc';

export default class ParentComponent extends LightningElement {

    @track childnumber;

    handleChild(event) {
        this.childnumber = event.detail.childnumber;
    }

}
```

#### Child Component 

The HTML and JS looks like this - 

```html
<template>
    <div style="background-color: #D3D3D3">
        <lightning-card title="Child Component">
            <div style="padding-left: 2rem;">Welcome, {username}</div>
            <br />
            <a style="padding-left: 2rem;" onclick={clickbutton}>Click here to get phone number</a>
        </lightning-card>
    </div>
</template>
```

```js
import { LightningElement, track, api } from 'lwc';

export default class ChildComponent extends LightningElement {
    @api username;

    clickbutton() {
        const event = new CustomEvent('child', {
            detail: { "childnumber": "+1-214-xxx-xxxx" }
        });
        this.dispatchEvent(event);
    }
}
```

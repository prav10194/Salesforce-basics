## From parent-to-child

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
export default class ChildComponent extends LightningElement {
    @api username;
}
```

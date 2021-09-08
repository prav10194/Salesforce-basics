## Adding a custom image data type in Lightning Datatable

#### Folder structures - 

![image](https://user-images.githubusercontent.com/8276139/132520998-942daeb9-b965-4d21-9eff-3db9e753392b.png)
![image](https://user-images.githubusercontent.com/8276139/132521030-e4b276f2-d69f-4f09-8e32-ac83ac68fe2e.png)
![image](https://user-images.githubusercontent.com/8276139/132521071-eb21e172-488c-411e-bc24-b6853ab5c875.png)

#### Components - 

HTML (main parent component) **testlwc.html** - 

```html
<template>
    <c-custom-image-data-table key-field="id" data={data} columns={columns}>
    </c-custom-image-data-table>
</template>
```

JS (main parent component) **testlwc.js**

```js
import { LightningElement, api, track } from "lwc";
import { OmniscriptBaseMixin } from "vlocity_cmt/omniscriptBaseMixin";

const columns = [
    {
        fieldName: 'patientProfileIcon',
        label: 'Profile Icon',
        type: 'image',
        typeAttributes: {
            imageurlvalue: { fieldName: 'imageurl' }
        }
    },
    { label: 'Patient Number', fieldName: 'patientNumberId' },
    { label: 'Patient Name', fieldName: 'patientName' }
]

const data = [{
    "id": "1",
    "patientNumberId": "872345",
    "patientName": "Kelly",
    "imageurl": "https://www.kindpng.com/picc/m/716-7168708_female-fill-circle-male-profile-icon-png-transparent.png",
}, {
    "id": "2",
    "patientNumberId": "776756",
    "patientName": "Charlie",
    "imageurl": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSFjrPp4410m5VXMUKg7NPACj-bbE9vcsJA9g&usqp=CAU",
}]

export default class Testlwc extends OmniscriptBaseMixin(LightningElement) {
    
    data = data;
    columns = columns;
    connectedCallback() {
        
    }
}
```

HTML (first child component main html) **customImageDataTable.html**

```html
<template>
</template>
```

HTML (first child component template html) **imageTableControl.html**

```html
<template>
    <c-image-control url={typeAttributes.imageurlvalue}
    alt-text="Image Not Found">
    </c-image-control>
</template>
```

JS (first child component main js) **customImageDataTable.js**

```js
import { api, track } from 'lwc';
import LightningDatatable from 'lightning/datatable';
import imageTableControl from './imageTableControl.html';

export default class SalesforceCodexDataTable extends LightningDatatable  {
    static customTypes = {
        image: {
            template: imageTableControl,
            typeAttributes: ['imageurlvalue'],
        }
    };
}
```

HTML (second child component main HTML) **imageControl.html**

```html
<template>
    <img style="padding: 4px; max-width: 50%; height: auto;" src={url} alt={altText} class="image"/>
</template>
```
JS (first child component main js) **imageControl.js**

```js
import { LightningElement,api } from 'lwc';

export default class ImageControl extends LightningElement {
    @api url;
    @api altText;
}
```

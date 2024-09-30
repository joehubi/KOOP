// functions.js

//#region ######### Funktionen für HTML in Java Script

// Funktion für die Pfaderstellung z.B. "Person_1/add"
function generatePersonPath(personNumber, action) {
    return `/Person_${personNumber}/${action}/`; // erstellt den Pfad für die folgenden Funktionen (z.B. "Person_1/add/")
}

// Hinzufügen von Artikeln/Einkäufen
function addItemManually2(personNumber) {
    var itemName = document.getElementById("artikel_id").value;
    var itemAmount = document.getElementById("stk_kg_id").value;
    var itemPrice = document.getElementById("preis_id").value;

    let formData = new FormData();
    formData.append('itemName', itemName);
    formData.append('itemAmount', itemAmount);
    formData.append('itemPrice', itemPrice);            
    formData.append('csrfmiddlewaretoken', token);

    fetch(generatePersonPath(personNumber, 'add'),{
        method: 'POST',
        body: formData
    });
}

// Löschen eines Artikels/Einkaufs
function deleteItem(personNumber) {

    let itemNumber = prompt('Nummer des Einkaufs der gelöscht werden soll')
    if (itemNumber === null) {
        return;
    }

    let formData = new FormData();
    formData.append('itemNumber', itemNumber);
    formData.append('csrfmiddlewaretoken', token);

    fetch(generatePersonPath(personNumber, 'delete'),{
        method: 'POST',
        body: formData
    });
}

// Bilden der Summe des aktuellen Einkaufs
function sum(personNumber) {

    let formData = new FormData();
    formData.append('csrfmiddlewaretoken', token);

    fetch(generatePersonPath(personNumber, 'sum'),{
        method: 'POST',
        body: formData
    });
}
//#endregion


//#region ########### Aktuell NICHT aktiv
function addItemAutomatic(personNumber) {
    let itemNumber = prompt('Nummer aus Preisliste auswählen')
    if (itemNumber === null) {
        return;
    }
    let itemAmount = prompt('Menge (kg oder Stück)')
    if (itemAmount === null) {
        return;
    }

    let formData = new FormData();
    formData.append('itemNumber', itemNumber);
    formData.append('itemAmount', itemAmount);
    formData.append('csrfmiddlewaretoken', token);

    fetch(generatePersonPath(personNumber, 'addSmart'),{
        method: 'POST',
        body: formData
    });
}

function addItemAutomatic2(personNumber) {
    var itemNumber = document.getElementById("id_preis").value;
    var itemAmount = document.getElementById("stk_kg").value;

    let formData = new FormData();
    formData.append('itemNumber', itemNumber);
    formData.append('itemAmount', itemAmount);
    formData.append('csrfmiddlewaretoken', token);

    fetch(generatePersonPath(personNumber, 'addSmart'),{
        method: 'POST',
        body: formData
    });
}

// with prompt
function addItemManually(personNumber) {
    let itemName = prompt('Name des Artikels')
    if (itemName === null) {
        return;
    }
    let itemAmount = prompt('Menge (kg oder Stück)')
    if (itemAmount === null) {
        return;
    }
    let itemPrice = prompt('Preis in €')
    if (itemPrice === null) {
        return;
    }
  
    let formData = new FormData();
    formData.append('itemName', itemName);
    formData.append('itemAmount', itemAmount);
    formData.append('itemPrice', itemPrice);            
    formData.append('csrfmiddlewaretoken', token);

    fetch(generatePersonPath(personNumber, 'add'),{
        method: 'POST',
        body: formData
    });
}
//#endregion


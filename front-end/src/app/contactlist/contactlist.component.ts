import { Component, OnInit } from '@angular/core';
import { StoreService } from '../services/store.service';

@Component({
  selector: 'app-contactlist',
  templateUrl: './contactlist.component.html',
  styleUrls: ['./contactlist.component.scss']
})
export class ContactlistComponent {

  auth: boolean;
  contacts = [];

  constructor(private store: StoreService) { 
    // load our contacts from our mock data
    this.auth = store.getLoggedIn();
    let names = this.store.getContacts();
    let numbers = this.store.getNumbers();
    for (var i = 0; i < names.length; i++) {
      this.contacts.push({phone: numbers[i], name: names[i]});
    }
    console.log(this.contacts);
  }

}

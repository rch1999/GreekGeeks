import { Component, OnInit } from '@angular/core';
import { StoreService } from '../services/store.service';
import { Contact } from '../models/contact.model';
import { Activity } from '../models/activity.model';

@Component({
  selector: 'app-feed',
  templateUrl: './feed.component.html',
  styleUrls: ['./feed.component.scss']
})
export class FeedComponent {
  auth: boolean;
  contacts = [];
  activities = [];

  constructor(private store: StoreService) { 
    // load our contacts from our mock data
    this.auth = store.getLoggedIn();
    let names = this.store.getContacts();
    let numbers = this.store.getNumbers();
    for (var i = 0; i < names.length; i++) {
      this.contacts.push({phone: numbers[i], name: names[i]});
    }
    // load our activities from our mock data
    let headers = this.store.getActivityHeaders();
    let texts = this.store.getActivityText();
    let types = this.store.getActivityType();
    for (var j = 0; j < headers.length; j++) {
      this.activities.push({header: headers[j], text: texts[j],
      type: types[j]});
    }
  }

}

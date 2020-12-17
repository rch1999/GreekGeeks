import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { User } from '../models/user.model';
import { StoreService } from '../services/store.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {

  @Input() email: string;
  @Input() password: string;
  errorMsg: string;

  constructor(private router: Router,
              private store: StoreService) {}

    login() {
      this.store.logIn();
      this.router.navigateByUrl('/feed'); // change this to feed
    }
}

import { Component, Input, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { User } from '../models/user.model';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {

  @Input() email: string;
  @Input() password: string;
  errorMsg: string;

  constructor(private router: Router) { }

    login() {
      this.router.navigateByUrl('/about');
    }
}

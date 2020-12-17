import { Component, Input } from '@angular/core';
import { Router } from '@angular/router';
import { User } from '../models/user.model';
import { StoreService } from '../services/store.service';
// import { AuthService } from '../services/auth/auth.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent {

  @Input() email: string;
  @Input() password: string;
  @Input() displayName: string;
  errorMsg: string;
  constructor(private router: Router,
              private store: StoreService) { }

    signUp() {
      this.store.logIn();
      this.router.navigateByUrl('/feed');
      console.log(this.store.getLoggedIn());
    }

    handleError(errMessage: string): void {
      this.errorMsg = errMessage;
    }
}
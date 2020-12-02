import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { ApiService } from '../services/api.service';

import { LoginComponent } from './login.component';

describe('LoginComponent', () => {
  let component: LoginComponent;
  let backend: ApiService;
  let fixture: ComponentFixture<LoginComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LoginComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LoginComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
    // clear all user info in the database between tests
    backend.clearUsers(); 
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  // make sure each fundamental variable has a starting value of ""
  it('should start with empty fields', () => {
    expect(component.email).toEqual("");
    expect(component.password).toEqual("");
  })

  // make sure we can't login with no info specified
  it('should prevent login without action taken', () => {
    expect(component.email).toEqual("");
    expect(component.password).toEqual("");

    // perform a login
    try {
      component.login();
    } catch (error) {
      expect(error).toEqual(new Error("Please properly specify your credentials."));
    }
  });

  // make sure you can log in with valid credentials
  it('should allow login on valid credentials', () => {

    // populate email and password with valid credentials
    component.email = backend.getUsers()[0].email;
    component.password = backend.getUsers()[0].email;

    // perform a login
    try {
      component.login();
    } catch (error) {
      console.log(error) // if this happens the test fails
    }
  });

  it('should prevent login with an invalid email', () => {

    // provide a horifically invalid email
    component.email = "invalid@invalid.com";
    component.password = "somepassword";

    // ensure that this email is not in our database/records
    expect(backend.getUserByEmail(component.email)).toBe(null);

    // perform a login
    try {
      component.login();
    } catch (error) {
      expect(error).toEqual(new Error("Email not in records"));
    }
  });

  it('should prevent login with an invalid password', () => {

    // provide an invalid password, null for example
    component.email = backend.getUsers()[0].username;
    component.password = null;

    // ensure that this email is a real email in our database
    expect(backend.getUserByEmail(component.email)).toBeTruthy();

    // perform a login
    try {
      component.login();
    } catch (error) {
      expect(error).toEqual(new Error("Invalid password"));
    }
  });
});

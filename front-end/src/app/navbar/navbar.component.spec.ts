import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { StoreService } from '../services/store.service';

import { NavbarComponent } from './navbar.component';

describe('NavbarComponent', () => {
  let component: NavbarComponent;
  let fixture: ComponentFixture<NavbarComponent>;
  let store: StoreService

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NavbarComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NavbarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should log user out upon logging out', () => {
    // first, we perform a logout via our navbar component
    component.logout();

    // we expect that our data store knows that we logged out
    expect(store.getLoggedIn()).toBe(false);
  });
});

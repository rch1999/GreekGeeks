import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FeedbarComponent } from './feedbar.component';

describe('FeedbarComponent', () => {
  let component: FeedbarComponent;
  let fixture: ComponentFixture<FeedbarComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FeedbarComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FeedbarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

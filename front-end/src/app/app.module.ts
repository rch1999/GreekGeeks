import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { appRoutes } from '../routes';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { SignupComponent } from './signup/signup.component';
import { LoginComponent } from './login/login.component';
import { AboutComponent } from './about/about.component';
import { NavbarComponent } from './navbar/navbar.component';
import { RouterModule } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { OrganizationComponent } from './organization/organization.component';
import { FeedComponent } from './feed/feed.component';
import { StoreService } from './services/store.service';
import { ContactComponent } from './contact/contact.component';
import { ContactlistComponent } from './contactlist/contactlist.component';
import { ActivityComponent } from './activity/activity.component';
import { FeedbarComponent } from './feedbar/feedbar.component';
import { ContactbarComponent } from './contactbar/contactbar.component';

@NgModule({
  declarations: [
    AppComponent,
    SignupComponent,
    LoginComponent,
    AboutComponent,
    NavbarComponent,
    OrganizationComponent,
    FeedComponent,
    ContactComponent,
    ContactlistComponent,
    ActivityComponent,
    FeedbarComponent,
    ContactbarComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule.forRoot(appRoutes),
    FormsModule
  ],
  providers: [StoreService],
  bootstrap: [AppComponent]
})
export class AppModule { }

import { Routes } from '@angular/router';
import { SignupComponent } from './app/signup/signup.component';
import { LoginComponent } from './app/login/login.component';
import { AboutComponent } from './app/about/about.component';
import { FeedComponent } from './app/feed/feed.component';

export const appRoutes: Routes = [
    {path: 'signup', component: SignupComponent},
    {path: 'login', component: LoginComponent},
    {path: 'about', component: AboutComponent},
    {path: 'feed', component: FeedComponent},
    {path: '', redirectTo: '/login', pathMatch: 'full'},
];
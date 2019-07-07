import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { NgModel } from '@angular/forms';

import { PassiveDialoguesComponent } from './passive-dialogues/passive-dialogues.component';
import { TableComponent } from './table/table.component';

const routes: Routes = [
    { path: '', component: TableComponent},
    { path: 'script', component: PassiveDialoguesComponent},
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule {}

export const routingComponents = [
    PassiveDialoguesComponent,
]
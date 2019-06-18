import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PassiveDialoguesComponent } from './passive-dialogues.component';

describe('PassiveDialoguesComponent', () => {
  let component: PassiveDialoguesComponent;
  let fixture: ComponentFixture<PassiveDialoguesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PassiveDialoguesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PassiveDialoguesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

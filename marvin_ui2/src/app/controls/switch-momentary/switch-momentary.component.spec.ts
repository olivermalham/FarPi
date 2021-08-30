import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { SwitchMomentaryComponent } from './switch-momentary.component';

describe('SwitchMomentaryComponent', () => {
  let component: SwitchMomentaryComponent;
  let fixture: ComponentFixture<SwitchMomentaryComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ SwitchMomentaryComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(SwitchMomentaryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

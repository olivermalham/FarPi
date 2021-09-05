import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DPadComponent } from './d-pad.component';

describe('DPadComponent', () => {
  let component: DPadComponent;
  let fixture: ComponentFixture<DPadComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DPadComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DPadComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

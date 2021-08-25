import { TestBed } from '@angular/core/testing';

import { FarPiHostService } from './far-pi-host.service';

describe('FarPiHostService', () => {
  let service: FarPiHostService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FarPiHostService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});

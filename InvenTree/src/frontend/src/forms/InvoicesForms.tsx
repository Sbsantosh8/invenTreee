import { useMemo } from 'react';
import { t } from '@lingui/macro';

export function useInvoiceFields() {
  console.log("invoice form rendered...")
  return useMemo(() => {
    return [
      {
        name: 'quotation_id',
        label: t`Quotation ID`,
        type: 'number',
        required: true
      },
      {
        name: 'lead_id',
        label: t`Lead ID`,
        type: 'number',
        required: true
      },
      {
        name: 'paid_amount',
        label: t`Paid Amount`,
        type: 'number',
        required: true
      },
      {
        name: 'due_date',
        label: t`Due Date`,
        type: 'datetime-local',
        required: true
      }
    ];
  }, []);
}


// import { useEffect, useState, useMemo } from 'react';
// import { t } from '@lingui/macro';
// import { AddItemButton } from '../../components/buttons/AddItemButton';
// import { formatCurrency } from '../../defaults/formatters';
// import { ApiEndpoints } from '../../enums/ApiEndpoints';
// import { ModelType } from '../../enums/ModelType';
// import { UserRoles } from '../../enums/Roles';
// import { useInvoiceFields } from '../../forms/InvoicesForms';
// import { useTable } from '../../hooks/UseTable';
// import { useCreateApiFormModal } from '../../hooks/UseForm';
// import { InvenTreeTable } from '../InvenTreeTable';
// import { useUserState } from '../../states/UserState';
// import InvoiceForm from '../../components/nav/Invoice'; // Import the InvoiceForm component from the correct path
// import '../../components/nav/Invoice.css'; // Import the CSS for InvoiceForm

// export function PaidInvoiceTable({
//   partId,
//   customerId
// }: Readonly<{
//   partId?: number;
//   customerId?: number;
// }>) {
//   const table = useTable(!!partId ? 'invoices-part' : 'invoices-index');
//   const user = useUserState();
//   const [invoices, setInvoices] = useState<any[]>([]);
//   const [leads, setLeads] = useState<Record<number, string>>({});
//   const [showInvoiceForm, setShowInvoiceForm] = useState(false); // State to control the visibility of the Invoice form

//   useEffect(() => {
//     fetchInvoices();
//     fetchLeads();
//   }, []);

//   const fetchLeads = async () => {
//     try {
//       const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/leads/');
//       const result = await response.json();
//       if (response.ok) {
//         const leadMap: Record<number, string> = {};
//         result.forEach((lead: any) => {
//           leadMap[lead.id] = lead.name;
//         });
//         setLeads(leadMap);
//         console.log('Fetched leads:', leadMap); // Log fetched leads
//       } else {
//         console.error('Failed to fetch leads:', result.error);
//       }
//     } catch (error) {
//       console.error('Error fetching leads:', error);
//     }
//   };

//   const fetchInvoices = async () => {
//     try {
//       const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/invoices/');
//       const result = await response.json();
//       if (response.ok) {
//         const paidInvoices = result.filter((invoice: any) => invoice.status === 'paid');
//         setInvoices(paidInvoices);
//         console.log('Fetched invoices:', paidInvoices); // Log fetched invoices
//       } else {
//         console.error('Failed to fetch invoices:', result.error);
//       }
//     } catch (error) {
//       console.error('Error fetching invoices:', error);
//     }
//   };

//   const newInvoice = useCreateApiFormModal({
//     url: ApiEndpoints.invoice_list,
//     title: t`Add Invoice`,
//     fields: useInvoiceFields(),
//     initialData: { customer: customerId },
//     follow: true,
//     modelType: ModelType.invoice
//   });

//   const tableActions = useMemo(() => {
//     return [
//       <AddItemButton
//         key='add-invoice'
//         tooltip={t`Add Invoice`}
//         onClick={() => setShowInvoiceForm(true)} // Open the Invoice form when the button is clicked
//         hidden={!user.hasAddRole(UserRoles.invoice)}
//       />
//     ];
//   }, [user]); 

//   const tableColumns = useMemo(() => {
//     return [
//       { accessor: 'quotation_number', title: t`Quotation Number` },
//       { accessor: 'invoice_number', title: t`Invoice Number` },
//       {
//         accessor: 'total_amount',
//         title: t`Total Amount`,
//         render: (record: any) => formatCurrency(record.total_amount)
//       },
//       {
//         accessor: 'status',
//         title: t`Status`,
//         render: (record: any) => getStatusDisplay(record.status)
//       },
//       { accessor: 'created_at', title: t`Created Date` },
//       {
//         accessor: 'lead_name',
//         title: t`Lead Name`,
//         render: (record: any) => leads[record.lead_id] || 'N/A'
//       },
//       { accessor: 'due_date', title: t`Due Date` }
//     ];
//   }, [invoices, leads]);

//   console.log('Table columns:', tableColumns); // Log table columns
//   console.log('Table data:', invoices); // Log table data

//   return (
//     <>
//       {showInvoiceForm && (
//         <InvoiceForm onClose={() => setShowInvoiceForm(false)} /> // Render the InvoiceForm component conditionally
//       )}
//       {!showInvoiceForm && (
//         <>
//           {newInvoice.modal}
//           <InvenTreeTable
//             url="" // Remove the API URL since we're passing filtered data manually
//             tableState={table}
//             columns={tableColumns}
//             tableData={invoices}
//             props={{
//               params: { part: partId, customer: customerId },
//               tableActions: tableActions,
//               modelType: ModelType.invoice,
//               enableSelection: true,
//               enableDownload: true,
//               enableReports: true
//             }}
//           />
//         </>
//       )}
//     </>
//   );
// }

// function getStatusDisplay(status: string): string {
//   switch (status) {
//     case 'partially_paid':
//       return 'Partially Paid';
//     case 'paid':
//       return 'Paid';
//     case 'unpaid':
//       return 'Unpaid';
//     default:
//       return status;
//   }
// }




// import { useEffect, useState, useMemo } from 'react';
// import { t } from '@lingui/macro';
// import { AddItemButton } from '../../components/buttons/AddItemButton';
// import { formatCurrency } from '../../defaults/formatters';
// import { ApiEndpoints } from '../../enums/ApiEndpoints';
// import { ModelType } from '../../enums/ModelType';
// import { UserRoles } from '../../enums/Roles';
// import { useInvoiceFields } from '../../forms/InvoicesForms';
// import { useTable } from '../../hooks/UseTable';
// import { useCreateApiFormModal } from '../../hooks/UseForm';
// import { InvenTreeTable } from '../InvenTreeTable';
// import { useUserState } from '../../states/UserState';
// import Invoice from '../../components/nav/invoice'; // Import the Invoice component
 
// export function PaidInvoiceTable({
//   partId,
//   customerId
// }: Readonly<{
//   partId?: number;
//   customerId?: number;
// }>) {
//   const table = useTable(!!partId ? 'invoices-part' : 'invoices-index');
//   const user = useUserState();
//   const [invoices, setInvoices] = useState<any[]>([]);
//   const [leads, setLeads] = useState<Record<number, string>>({});
//   const [showInvoiceForm, setShowInvoiceForm] = useState(false); // State to control the visibility of the Invoice form
 
//   useEffect(() => {
//     fetchInvoices();
//     fetchLeads();
//   }, []);
 
//   const fetchLeads = async () => {
//     try {
//       const response = await fetch('http://127.0.0.1:8000/api/lead_to_invoice/leads/');
//       const result = await response.json();
//       if (response.ok) {
//         const leadMap: Record<number, string> = {};
//         result.forEach((lead: any) => {
//           leadMap[lead.id] = lead.name;
//         });
//         setLeads(leadMap);
//       } else {
//         console.error('Failed to fetch leads:', result.error);
//       }
//     } catch (error) {
//       console.error('Error fetching leads:', error);
//     }
//   };
 
//   const fetchInvoices = async () => {
//     try {
//       const response = await fetch('http://127.0.0.1:8000/api/lead_to_invoice/invoices/');
//       const result = await response.json();
//       if (response.ok) {
//         const paidInvoices = result.filter((invoice: any) => invoice.status === 'paid');
//         setInvoices(paidInvoices);
//       } else {
//         console.error('Failed to fetch invoices:', result.error);
//       }
//     } catch (error) {
//       console.error('Error fetching invoices:', error);
//     }
//   };
 
//   const newInvoice = useCreateApiFormModal({
//     url: ApiEndpoints.invoice_list,
//     title: t`Add Invoice`,
//     fields: useInvoiceFields(),
//     initialData: { customer: customerId },
//     follow: true,
//     modelType: ModelType.invoice
//   });
 
//   const tableActions = useMemo(() => {
//     return [
//       <AddItemButton
//         key='add-invoice'
//         tooltip={t`Add Invoice`}
//         onClick={() => setShowInvoiceForm(true)} // Open the Invoice form when the button is clicked
//         hidden={!user.hasAddRole(UserRoles.invoice)}
//       />
//     ];
//   }, [user]);
 
//   const tableColumns = useMemo(() => {
//     return [
//       { accessor: 'quotation_number', title: t`Quotation Number` },
//       { accessor: 'invoice_number', title: t`Invoice Number` },
//       {
//         accessor: 'total_amount',
//         title: t`Total Amount`,
//         render: (record: any) => formatCurrency(record.total_amount)
//       },
//       {
//         accessor: 'status',
//         title: t`Status`,
//         render: (record: any) => getStatusDisplay(record.status)
//       },
//       { accessor: 'created_at', title: t`Created Date` },
//       {
//         accessor: 'lead_name',
//         title: t`Lead Name`,
//         render: (record: any) => leads[record.lead_id] || 'N/A'
//       },
//       { accessor: 'due_date', title: t`Due Date` }
//     ];
//   }, [invoices, leads]);
 
//   return (
//     <>
//       {showInvoiceForm && (
//         <Invoice onClose={() => setShowInvoiceForm(false)} /> // Render the Invoice component conditionally
//       )}
//       {!showInvoiceForm && (
//         <>
//           {newInvoice.modal}
//           <InvenTreeTable
//             url="" // Remove the API URL since we're passing filtered data manually
//             tableState={table}
//             columns={tableColumns}
//             tableData={invoices}
//             props={{
//               params: { part: partId, customer: customerId },
//               tableActions: tableActions,
//               modelType: ModelType.invoice,
//               enableSelection: true,
//               enableDownload: true,
//               enableReports: true
//             }}
//           />
//         </>
//       )}
//     </>
//   );
// }
 
// function getStatusDisplay(status: string): string {
//   switch (status) {
//     case 'partially_paid':
//       return 'Partially Paid';
//     case 'paid':
//       return 'Paid';
//     case 'unpaid':
//       return 'Unpaid';
//     default:
//       return status;
//   }
// }




import { useEffect, useState, useMemo } from 'react';
import { t } from '@lingui/macro';
import { AddItemButton } from '../../components/buttons/AddItemButton';
import { formatCurrency } from '../../defaults/formatters';
import { ApiEndpoints } from '../../enums/ApiEndpoints';
import { ModelType } from '../../enums/ModelType';
import { UserRoles } from '../../enums/Roles';
import { useInvoiceFields } from '../../forms/InvoicesForms';
import { useTable } from '../../hooks/UseTable';
import { useCreateApiFormModal } from '../../hooks/UseForm';
import { InvenTreeTable } from '../InvenTreeTable';
import { useUserState } from '../../states/UserState';
import Invoice from '../../components/nav/Invoice'; // Import the Invoice component
 
export default function PaidInvoiceTable({
  partId,
  customerId
}: Readonly<{
  partId?: number;
  customerId?: number;
}>) {
  const table = useTable(!!partId ? 'invoices-part' : 'invoices-index');
  const user = useUserState();
  const [invoices, setInvoices] = useState<any[]>([]);
  const [leads, setLeads] = useState<Record<number, string>>({});
  const [showInvoiceForm, setShowInvoiceForm] = useState(false); // State to control the visibility of the Invoice form
 
  useEffect(() => {
    fetchInvoices();
    fetchLeads();
  }, []);
 
  const fetchLeads = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/leads/');
      const result = await response.json();
      if (response.ok) {
        const leadMap: Record<number, string> = {};
        result.forEach((lead: any) => {
          leadMap[lead.id] = lead.name;
        });
        setLeads(leadMap);
      } else {
        console.error('Failed to fetch leads:', result.error);
      }
    } catch (error) {
      console.error('Error fetching leads:', error);
    }
  };
 
  const fetchInvoices = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/lead-to-invoice/invoices/');
      const result = await response.json();
      if (response.ok) {
        const paidInvoices = result.filter((invoice: any) => invoice.status === 'paid');
        setInvoices(paidInvoices);
      } else {
        console.error('Failed to fetch invoices:', result.error);
      }
    } catch (error) {
      console.error('Error fetching invoices:', error);
    }
  };
 
  const newInvoice = useCreateApiFormModal({
    url: ApiEndpoints.invoice_list,
    title: t`Add Invoice`,
    fields: useInvoiceFields(),
    initialData: { customer: customerId },
    follow: true,
    modelType: ModelType.invoice
  });
 
  const tableActions = useMemo(() => {
    return [
      <AddItemButton
        key='add-invoice'
        tooltip={t`Add Invoice`}
        onClick={() => setShowInvoiceForm(true)} // Open the Invoice form when the button is clicked
        hidden={!user.hasAddRole(UserRoles.invoice)}
      />
    ];
  }, [user]);
 
  const tableColumns = useMemo(() => {
    return [
      { accessor: 'quotation_number', title: t`Quotation Number` },
      { accessor: 'invoice_number', title: t`Invoice Number` },
      {
        accessor: 'total_amount',
        title: t`Total Amount`,
        render: (record: any) => formatCurrency(record.total_amount)
      },
      {
        accessor: 'status',
        title: t`Status`,
        render: (record: any) => getStatusDisplay(record.status)
      },
      { accessor: 'created_at', title: t`Created Date` },
      {
        accessor: 'lead_name',
        title: t`Lead Name`,
        render: (record: any) => leads[record.lead] || 'N/A'
      },
      { accessor: 'due_date', title: t`Due Date` }
    ];
  }, [invoices, leads]);
 
  return (
    <>
      {showInvoiceForm && (
        <Invoice onClose={() => setShowInvoiceForm(false)} /> // Render the Invoice component conditionally
      )}
      {!showInvoiceForm && (
        <>
          {newInvoice.modal}
          <InvenTreeTable
            url="" // Remove the API URL since we're passing filtered data manually
            tableState={table}
            columns={tableColumns}
            tableData={invoices}
            props={{
              params: { part: partId, customer: customerId },
              tableActions: tableActions,
              modelType: ModelType.invoice,
              enableSelection: true,
              enableDownload: true,
              enableReports: true
            }}
          />
        </>
      )}
    </>
  );
}
 
function getStatusDisplay(status: string): string {
  switch (status) {
    case 'partially_paid':
      return 'Partially Paid';
    case 'paid':
      return 'Paid';
    case 'unpaid':
      return 'Unpaid';
    default:
      return status;
  }
}

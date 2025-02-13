// // // import { t } from '@lingui/macro';
// // // import { Stack } from '@mantine/core';
// // // import {
// // //   IconBuildingStore,
// // //   IconTruckDelivery,
// // //   IconTruckReturn
// // // } from '@tabler/icons-react';
// // // import { useMemo } from 'react';

// // // import PermissionDenied from '../../components/errors/PermissionDenied';
// // // import { PageDetail } from '../../components/nav/PageDetail';
// // // import { PanelGroup } from '../../components/panels/PanelGroup';
// // // import { UserRoles } from '../../enums/Roles';
// // // import { useUserState } from '../../states/UserState';
// // // import { CompanyTable } from '../../tables/company/CompanyTable';
// // // import { ReturnOrderTable } from '../../tables/sales/ReturnOrderTable';
// // // import { SalesOrderTable } from '../../tables/sales/SalesOrderTable';

// // // export default function PurchasingIndex() {
// // //   const user = useUserState();

// // //   const panels = useMemo(() => {
// // //     return [
// // //       {
// // //         name: 'salesorders',
// // //         label: t`Sales Orders`,
// // //         icon: <IconTruckDelivery />,
// // //         content: <SalesOrderTable />,
// // //         hidden: !user.hasViewRole(UserRoles.sales_order)
// // //       },
// // //       {
// // //         name: 'returnorders',
// // //         label: t`Return Orders`,
// // //         icon: <IconTruckReturn />,
// // //         content: <ReturnOrderTable />,
// // //         hidden: !user.hasViewRole(UserRoles.return_order)
// // //       },
// // //       {
// // //         name: 'suppliers',
// // //         label: t`Customers`,
// // //         icon: <IconBuildingStore />,
// // //         content: (
// // //           <CompanyTable path='sales/customer' params={{ is_customer: true }} />
// // //         )
// // //       }
// // //     ];
// // //   }, [user]);

// // //   if (!user.isLoggedIn() || !user.hasViewRole(UserRoles.sales_order)) {
// // //     return <PermissionDenied />;
// // //   }

// // //   return (
// // //     <Stack>
// // //       <PageDetail title={t`Sales`} />
// // //       <PanelGroup
// // //         pageKey='sales-index'
// // //         panels={panels}
// // //         model={'sales'}
// // //         id={null}
// // //       />
// // //     </Stack>
// // //   );
// // // }


// // import { t } from '@lingui/macro';
// // import { Stack } from '@mantine/core';
// // import {
// //   IconBuildingStore,
// //   IconTruckDelivery,
// //   IconTruckReturn
// // } from '@tabler/icons-react';
// // import { useMemo } from 'react';

// // import PermissionDenied from '../../components/errors/PermissionDenied';
// // import { PageDetail } from '../../components/nav/PageDetail';
// // import { PanelGroup } from '../../components/panels/PanelGroup';
// // import { UserRoles } from '../../enums/Roles';
// // import { useUserState } from '../../states/UserState';
// // import { CompanyTable } from '../../tables/company/CompanyTable';
// // import { ReturnOrderTable } from '../../tables/sales/ReturnOrderTable';
// // import { SalesOrderTable } from '../../tables/sales/SalesOrderTable';

// // export default function SalesIndex() {
// //   const user = useUserState();

// //   const panels = useMemo(() => {
// //     return [
// //       {
// //         name: 'returnorders',
// //         label: t`Return Orders`,
// //         icon: <IconTruckReturn />,
// //         content: <ReturnOrderTable />,
// //         hidden: !user.hasViewRole(UserRoles.return_order)
// //       },
// //       {
// //         name: 'salesorders',
// //         label: t`Sales Orders`,
// //         icon: <IconTruckDelivery />,
// //         content: <SalesOrderTable />,
// //         hidden: !user.hasViewRole(UserRoles.sales_order)
// //       },
// //       {
// //         name: 'suppliers',
// //         label: t`Customers`,
// //         icon: <IconBuildingStore />,
// //         content: (
// //           <CompanyTable path='sales/customer' params={{ is_customer: true }} />
// //         )
// //       }
// //     ];
// //   }, [user]);

// //   if (!user.isLoggedIn() || (!user.hasViewRole(UserRoles.sales_order) && !user.hasViewRole(UserRoles.return_order))) {
// //     return <PermissionDenied />;
// //   }

// //   return (
// //     <Stack>
// //       <PageDetail title={t`Sales`} />
// //       <PanelGroup
// //         pageKey='sales-index'
// //         panels={panels}
// //         model={'sales'}
// //         id={null}
// //         // defaultPanel='returnorders' // Set the default panel to 'returnorders'
// //       />
// //     </Stack>
// //   );
// // }



// import { t } from '@lingui/macro';
// import { Stack } from '@mantine/core';
// import {
//   IconBuildingStore,
//   IconTruckDelivery,
//   IconTruckReturn
// } from '@tabler/icons-react';
// import { useMemo } from 'react';

// import PermissionDenied from '../../components/errors/PermissionDenied';
// import { PageDetail } from '../../components/nav/PageDetail';
// import { PanelGroup } from '../../components/panels/PanelGroup';
// import { UserRoles } from '../../enums/Roles';
// import { useUserState } from '../../states/UserState';
// import { CompanyTable } from '../../tables/company/CompanyTable';
// import { ReturnOrderTable } from '../../tables/sales/ReturnOrderTable';
// import { SalesOrderTable } from '../../tables/sales/SalesOrderTable';

// export default function SalesIndex() {
//   const user = useUserState();

//   const panels = useMemo(() => {
//     return [
//       {
//         name: 'returnorders',
//         label: t`Return Orders`,
//         icon: <IconTruckReturn />,
//         content: <ReturnOrderTable />,
//         hidden: !user.hasViewRole(UserRoles.return_order)
//       },
//       // {
//       //   name: 'salesorders',
//       //   label: t`Sales Orders`,
//       //   icon: <IconTruckDelivery />,
//       //   content: <SalesOrderTable />,
//       //   hidden: !user.hasViewRole(UserRoles.sales_order)
//       // },
//       {
//         name: 'suppliers',
//         label: t`Customers`,
//         icon: <IconBuildingStore />,
//         content: (
//           <CompanyTable path='sales/customer' params={{ is_customer: true }} />
//         )
//       }
//     ];
//   }, [user]);

//   if (!user.isLoggedIn() || (!user.hasViewRole(UserRoles.sales_order) && !user.hasViewRole(UserRoles.return_order))) {
//     return <PermissionDenied />;
//   }

//   return (
//     <Stack>
//       <PageDetail title={t`Sales`} />
//       <PanelGroup
//         pageKey='sales-index'
//         panels={panels}
//         model={'sales'}
//         id={null}
//       />
//     </Stack>
//   );
// }



import { t } from '@lingui/macro';
import { Stack } from '@mantine/core';
import {
  IconBuildingStore,
  IconTruckDelivery,
  IconTruckReturn
} from '@tabler/icons-react';
import { useMemo } from 'react';

import PermissionDenied from '../../components/errors/PermissionDenied';
import { PageDetail } from '../../components/nav/PageDetail';
import { PanelGroup } from '../../components/panels/PanelGroup';
import { UserRoles } from '../../enums/Roles';
import { useUserState } from '../../states/UserState';
import { CompanyTable } from '../../tables/company/CompanyTable';
import { ReturnOrderTable } from '../../tables/sales/ReturnOrderTable';
import { SalesOrderTable } from '../../tables/sales/SalesOrderTable';

export default function SalesIndex() {
  const user = useUserState();
  console.log("sales index page : frm pages .....")
  const panels = useMemo(() => {
    return [
  
      {
        name: 'salesorders',
        label: t`Sales Orders`,
        icon: <IconTruckDelivery />,
        content: <SalesOrderTable />,
        hidden: !user.hasViewRole(UserRoles.sales_order)
      },
          {
        name: 'returnorders',
        label: t`Return Orders`,
        icon: <IconTruckReturn />,
        content: <ReturnOrderTable />,
        hidden: !user.hasViewRole(UserRoles.return_order)
      },
      {
        name: 'suppliers',
        label: t`Customers`,
        icon: <IconBuildingStore />,
        content: (
          <CompanyTable path='sales/customer' params={{ is_customer: true }} />
        )
      }
    ];
  }, [user]);

  if (!user.isLoggedIn() || (!user.hasViewRole(UserRoles.sales_order) && !user.hasViewRole(UserRoles.return_order))) {
    return <PermissionDenied />;
  }

  return (
    <Stack>
      <PageDetail title={t`Sales`} />
      <PanelGroup
        pageKey='sales-index'
        panels={panels}
        model={'sales'}
        id={null}
        
      />
    </Stack>
  );
}
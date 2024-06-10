<template>
    <!-- source:https://codepen.io/owaiswiz/pen/jOPvEPB -->

   
                     
                       <div class="mx-auto max-w-xs">
                           <input
                               class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white"
                               type="text" placeholder="Nombre Completo" 
                               
                            />
                           <input
                               class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
                               type="text" placeholder="Primer Apellido" 
                           />
                           <input
                               class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
                               type="text" placeholder="Segundo Apellido" 
                           />
                           <input
                               class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
                               type="date" placeholder="dd/mm/aaaa" 
                           />
                          
                           <form class="max-w-sm mx-auto">
                             <select id="countries" class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5">
                               <option selected>Tipo de Sangre</option>
                               <option value="A+">A+</option>
                               <option value="A-">O+</option>
                               <option value="B+">B+</option>
                               <option value="AB+">AB+</option>
                               <option value="A-">A-</option>
                               <option value="O-">O-</option>
                               <option value="B-">B-</option>
                               <option value="AB-">Ab-</option>
                             </select>
                           </form>
   
                           <input
                               class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5"
                               type="email" placeholder="Email" 
                           />
                           <input
                               class="w-full px-8 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-5 mb-5"
                               type="password" placeholder="Password" 
                           />
   
                           <label class="font-medium">Fotografia</label>
                           
                           <input
                               class="w-full px-1 py-4 rounded-lg font-medium bg-gray-100 border border-gray-200 placeholder-gray-500 text-sm focus:outline-none focus:border-gray-400 focus:bg-white mt-1 "
                               type="file" placeholder="Foto" 
                           />
                           
                       </div>
                   
   </template>